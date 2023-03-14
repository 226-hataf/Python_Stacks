const express=require("express")
const userRoute= express.Router()
const auth= require("../middleware/auth")
const {user}= require("../controller/user_controller")

userRoute.get("/user", auth, user ) // final url {http://localhost:3000/user}

module.exports=userRoute