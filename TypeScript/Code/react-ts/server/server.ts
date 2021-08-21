import http from "http"
import express from "express"
import logging from "./config/logging"
import config from "./config/config"
import mongoose from "mongoose"
import firebaseAdmin from "firebase-admin"

const router = express()

const httpServer = http.createServer(router)

let serviveAccountKey = require("./config/serviceAccountKey.json")

firebaseAdmin.initializeApp({
    credential: firebaseAdmin.credential.cert(serviveAccountKey)
})

mongoose.connect(config.mongo.url)
    .then(() => {
        console.log("MongoDb connect succes")
    })
    .catch((err) => {
        console.log(err)
    })

router.use(express.urlencoded({ extended: true }))
router.use(express.json())

router.use((req, res, next) => {
    const error = new Error("Not Found")
    return res.status(404).json({
        message: error.message
    })
})

httpServer.listen(2704, () => {
    console.log("succes")
})