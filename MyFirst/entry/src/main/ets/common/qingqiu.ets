import { http } from '@kit.NetworkKit';


export  function qingqiu(){
  // export function httpRequestGet(){
  let httpRequest = http.createHttp();
  let promise = httpRequest.request('http://127.0.0.1:5000/data_list',{
    method:http.RequestMethod.GET,
  })
  console.log(JSON.stringify(promise.then()))

  // }
}
