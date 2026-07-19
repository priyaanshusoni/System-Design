// Sliding Window Log Algorithm

const express = require("express");
const { rateLimiter } = require("./rate-limiter");
const app = express();

app.use(express.json());

const userMap = new Map();

const rateLimiterMiddleware = (req, res, next) => {
  try {
    const { status } = rateLimiter({
      key: req?.socket?.remoteAddress,
      store: userMap,
      window: 10 * 1000, //
      max_requests_allowed: 5,
    });

    if (status === 429) {
      return res.status(status).json({
        message: "Too Many requests , please wait for a while",
      });
    }

    return next();
  } catch (error) {
    console.error("Error", error);
  }
};

app.get("/api", rateLimiterMiddleware, (req, res) => {
  return res.status(200).json({ message: "Request successful" });
});

app.listen(3000, () => {
  console.log(`Server Started !`);
});
