


function getValue() {

  const currency = document.getElementById('selection');
  const dateTime = Date();
  const date = dateTime.slice(0, 10);
  const year = dateTime.slice(11, 15);
  const time = dateTime.slice(16, 28);
  document.getElementById('time').innerHTML = time + '<br>' +
    date + '<br>' + year;

  getData();

  async function getData() {

    const response = await fetch('https://api.coindesk.com/v1/bpi/currentprice.json');
    const data = await response.json();
    const conversion = data['bpi'][currency.value]['rate'];
    document.getElementById('conversion').innerHTML = 'One Bitcoin is worth:' + '<br>' +
      conversion.split('.')[0] + ' ' + currency.value;

  }
}
