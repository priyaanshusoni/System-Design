const rateLimiter = ({ key, store, max_requests_allowed, window }) => {
  const currentTimestamp = Date.now();

  let userTimestamps = store.get(key);

  if (!userTimestamps) {
    store.set(key, [currentTimestamp]);
    return {
      status: 200,
    };
  }

  const allowedRequests = userTimestamps.filter(
    (ts) => ts > currentTimestamp - window,
  );

  if (allowedRequests?.length < max_requests_allowed) {
    allowedRequests.push(currentTimestamp);
    store.set(key, allowedRequests);

    return {
      status: 200,
    };
  }

  return {
    status: 429,
  };
};

module.exports = {
  rateLimiter,
};
