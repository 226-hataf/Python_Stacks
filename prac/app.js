// console.log(module)
// let a=10;
// let c="ali"
// module.exports={a, c}
// console.log(module)
const express= require("express")
const app= express()
// const {user}=require("./controller/user_controller")
// const auth=require("./middleware/auth")
// app.get("/", auth,user )
const userRoute= require("./route/user_route")
app.use("/", userRoute) 
// final url {http://localhost:3000/user}



const port =3000
app.listen(port,()=>console.log(`server is runing on Port ${port}`))
