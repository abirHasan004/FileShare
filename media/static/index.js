const file=document.getElementById('file')
btn=document.getElementById('button1')

 
btn.addEventListener('click',(e)=>{
 
    e.preventDefault();
    formdata= new FormData()
    let files=file.files
    console.log(files)
    for(let i=0; i<files.length;i++){
        formdata.append('files',files[i])
        fetch('/home',{
            method:'POST',
            header:{'X_CSRFToken': '{{crsf_token}}'},
            body:formdata
    
        }) 
    
        
    }


 
}) 
// function myFun(e){
//     console.log('HELLO ')
//     console.log('file.Files')

// }