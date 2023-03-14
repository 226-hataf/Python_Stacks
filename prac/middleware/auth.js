function auth(req, res, next){
    console.log(" middleware called")
    next()

}
module.exports=auth
