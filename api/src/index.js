import express from 'express';
import dotenv from 'dotenv';
import cors from 'cors';
import models from './models/index.js';
import routes from './routes/index.js';

dotenv.config();

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Custom Middleware to pass models to routes
app.use((req, res, next) => {
  req.context = {
    models,
  };
  next();
});

// Mounting routes
app.use('/messages', routes.message);

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
