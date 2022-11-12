
//const sqlite3 = required('sqlite3').verbose();
//let db = new sqlite3.Database(':memory:');
const password = document.getElementById('password')
const email = document.getElementById('email')

document.getElementById('form').addEventListener('submit',(event) => {
  event.preventDefault()
  valid = true
//   add you check here :
  const password_value = password.value
  const email_value = email.value

  if (email_value.length < 5 || password_value.length < 12){
    alert ('The form has not been submitted : \n - A field is not valid ')
    valid= false
  }
  if (valid)
  alert('the form has been completed. \n we will proceed with the sending.')
  // submit the form if everything is valid :
  // if (valid ) event.target.submit();
})
// signup page
const email = document.getElementById('email')
const favorite_color = document.getElementById('favorite_color')
const password = document.getElementById('password')


document.getElementById('form').addEventListener('submit',(event) => {
  event.preventDefault()
  valid = true
//   add you check here :
  const email_value = email.value
  const favorite_color_value =  favorite_color.value
  const password_value = password.value


  if (email_value.length == '' || favorite_color.length == '' password_value.length == ''){
    alert ('The form has not been submitted : \n - A field is not valid ')
    valid= false
  }
  else (valid)
  alert('the form has been completed. \n we will proceed with the sending.')
  // submit the form if everything is valid :
  // if (valid ) event.target.submit();
})