import redis from 'redis';

const subscriberClient = redis.createClient();

subscriberClient.on('connect', () => {
    console.log('Redis client connected to the server');

    subscriberClient.subscribe('holberton school channel');
});

subscriberClient.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

subscriberClient.on('message', (channel, message) => {
    console.log(message);

    if (message === 'KILL_SERVER') {
        subscriberClient.unsubscribe('holberton school channel');
        subscriberClient.quit();
    }
});
