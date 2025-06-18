import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();

  before(() => {
    // kue.Job.rangeByType = kue.Job.rangeByType || (() => []);
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not-an-array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '1234567890',
        message: 'Test message 1'
      },
      {
        phoneNumber: '9876543210',
        message: 'Test message 2'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Test that 2 jobs were created
    expect(queue.testMode.jobs.length).to.equal(2);
    
    queue.testMode.jobs.forEach((job, index) => {
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.deep.equal(jobs[index]);
    });
  });
});
