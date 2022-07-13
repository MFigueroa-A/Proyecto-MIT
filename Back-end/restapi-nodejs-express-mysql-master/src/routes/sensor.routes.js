import { Router } from "express";
import { methods as sensorController } from "../controllers/sensor.controller";

const router = Router();

router.get("/", sensorController.getSensores);
/*router.get("/:id", languageController.getLanguage);
router.post("/", languageController.addLanguage);
router.put("/:id", languageController.updateLanguage);
router.delete("/:id", languageController.deleteLanguage);*/

export default router;
