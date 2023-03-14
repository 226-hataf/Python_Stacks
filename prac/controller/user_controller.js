
const users=[
    {
        name:"Usman",
        age:23,
        field:"MERN"

},
{
    name:"abubaker",
    age:23,
    field:"MERN"
},
{
    name:"Usman",
    age:23,
    field:"MERN"
}]

const user=(req,res)=>{
    console.log("end result")
    res.json(users)
}
module.exports={user}