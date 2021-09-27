const form = document.getElementById("comment")

const comment = document.getElementById("id_comment")
const csrf = document.getElementsByName("csrfmiddlewaretoken")


// submit our form

const url = ""

form.addEventListener("submit", e => {
    e.preventDefault()
    
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('comment', comment.value)

    $.ajax({
        type : 'POST',
        url : url,
        enctype : "multipart/form-data",
        data : fd,
        success : (response) => {
            console.log(response);
            setInterval('location.reload()', 500)
        },
        error : (error) => {
            console.log(error);
        },
        cache:false,
        contentType : false,
        processData : false,

        

    })
})