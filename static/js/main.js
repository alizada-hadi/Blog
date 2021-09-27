$(document).ready(() => {
    $('.like-form').submit(function(e){ 
        e.preventDefault()

        const post_id = $(this).attr('id')
        const likeText = $(`.like-btn${post_id}`).text()
        const trim = $.trim(likeText)
        const url = $(this).attr('action')
        
        let result
        const likes = $(`.like-count${post_id}`).text()
        const trimCount = parseInt(likes)

        $.ajax({
            type : "POST",
            url : url,
            data : {
                'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
                'post_id':post_id,
            },
            success : function(response){
                if(trim === 'Unlike'){
                    $(`.like-btn${post_id}`).text('Like')
                    result = trimCount - 1
                }
                else{
                    $(`.like-btn${post_id}`).text('Unlike')
                    result = trimCount + 1
                }
                $(`.like-count${post_id}`).text(result)
            },
            error : function(error){
                console.log(error);
            }
        })
    })
})



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


