const script = document.createElement('script');
 script.src = '//code.jquery.com/jquery-1.11.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);
function fun1(){
    const name = document.getElementById('name1');
    if(name.value === "")
        return false;
    const age = document.getElementById('age');
    const job = document.getElementById('job');
    const default1 = document.getElementById('default1');
    const balance = document.getElementById('balance');
    const housing = document.getElementById('housing');
    const month = document.getElementById('month');
    const duration = document.getElementById('duration');
    if(duration.value === "")
        return false;
    const poutcome = document.getElementById('poutcome');
    console.log(age.value);
    console.log(job.value);
    console.log(default1.value);
    console.log(balance.value);
    console.log(housing.value);
    console.log(month.value);
    console.log(duration.value);
    console.log(poutcome.value);
    const out1 = document.getElementById('output');

    const url="http://127.0.0.1:5000/predict_outcome";
    $.post(url, {
              age:age.value,
              job:job.value,
              default1:default1.value,
              housing:housing.value,
              poutcome:poutcome.value,
              month:month.value,
              balance:balance.value,
              duration:duration.value
            }, function(data, status) {
              out1.innerHTML=data.estimated_outcome.toString();
        });
}