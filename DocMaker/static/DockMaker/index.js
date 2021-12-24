document.addEventListener('DOMContentLoaded',function (){


      document.querySelector('.btn.btn-lg.btn-primary.all-experiment-button').addEventListener('click',load_experiments);




  // By default, load the inbox
  load_mainpage();



});


function load_mainpage() {

  // Show the mailbox and hide other views
  document.querySelector('#experiment-section').style.display = 'none';
  document.querySelector('#main-container').style.display = 'block';

}




function load_experiments() {


  document.querySelector('#main-container').style.display ='none';
  // Show the mailbox and hide other views
  document.querySelector('#experiment-section').style.display ='block';


}