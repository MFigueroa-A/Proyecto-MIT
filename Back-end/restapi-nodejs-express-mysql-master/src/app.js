import express from "express";
import morgan from "morgan";
// Routes
import sensorRoutes from "./routes/sensor.routes";

const app = express();

// Settings
app.set("port", 8091);

// Middlewares
app.use(morgan("dev"));
app.use(express.json());

// Routes
app.use("/api/sensores", sensorRoutes);

export default app;
