const express=require('express');
const upload=require('express-fileupload')

const app=express()

app.use(upload())

app.get('/',(req,res)=>{
	res.sendFile(__dirname+'/index.html')
})

app.post('/',(req,res)=>{
	if(req.files)
	{
		console.log(req.files)
		var file=req.files.Thefile
		var name=file.name
		console.log(name)
		file.mv('E:/Veritas/Files/'+name,function(err){
			if(err)
			{
				res.send(err)
			}
			else
			{
				res.send("File has been addded to the Veritas Folder")
			}
		})
	}
})
var PORT=5500
app.listen(PORT, function(err){
    if (err) console.log("Error in server setup")
    console.log("Server listening on Port", PORT);
})