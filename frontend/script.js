async function predictWeather(){


let city =
document.getElementById(
"city"
).value;



let response =
await fetch(

`http://127.0.0.1:8000/predict_city/${city}`

);



let data =
await response.json();

console.log(data);



document.getElementById(
"result"
).innerHTML
=


`

<div class="card">

<h2>
📍 ${data.city}
</h2>


🌡 Temperature:

${data.current_weather.temp} °C


<br>


💧 Humidity:

${data.current_weather.humidity}%


<br>


🌬 Wind:

${data.current_weather.windspeed} m/s


</div>



<div class="card ai">


<h2>
🤖 AI Prediction
</h2>


Tomorrow Temperature:

<h1>

${data["Tomorrow Prediction"]} °C

</h1>


</div>


`;


}