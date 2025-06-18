import express from 'express';
import kue from 'kue';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const queue = kue.createQueue();

const client = createClient();
client.on('error', (err) => console.error('Redis Client Error', err));

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

let reservationEnabled = true;

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
}

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (!err) res.json({ status: 'Reservation in process' });
    else res.json({ status: 'Reservation failed' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();
    if (availableSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }
    availableSeats -= 1;
    await reserveSeat(availableSeats);
    if (availableSeats === 0) reservationEnabled = false;
    done();
  });
});

app.listen(port, async () => {
  await reserveSeat(50);
  console.log(`API available on localhost port ${port}`);
});
