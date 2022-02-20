let addToCart = document.getElementsByClassName('addCart')
for(let i=0; i < addToCart.length; i++){

    addToCart[i].addEventListener('click', function(){
        let productId = this.dataset.product
        let action = this.dataset.action
        let qty = this.dataset.qty


 
    let url = '/update_cart/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' :  csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action, 'qty':qty})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
        // console.log('DataToSend:', productId)
        // console.log('DataToSend:', action)
        // console.log('DataToSend:', qty)
    })

}