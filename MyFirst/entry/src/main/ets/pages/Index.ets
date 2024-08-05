import {qingqiu} from '../common/qingqiu'
import { http } from '@kit.NetworkKit';
import { data } from '@kit.TelephonyKit';
import { router, Router } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State data:string = '123'
  @State message: string = '吾爱热榜';
  @State col: string = '#ff0000';
  zhihu(){

    let httpRequest = http.createHttp();
    let promise = httpRequest.request('http://127.0.0.1:5000/data_list',{
      method:http.RequestMethod.GET,
    },(err,data)=>{
      let json_data = JSON.stringify(data.result)
      console.info("data:"+json_data);
      this.data = json_data
      router.pushUrl({
        url: 'pages/detail',
        params: { data:this.data }
      })
    })

  }
  faxian(){
    // router.pushUrl({
    //   url: 'pages/Index',
    //   params: { data:this.data }
    // })
  }


  build() {

    RelativeContainer() {
      Column(){
        Row(){
          Image($r("app.media.rebang"))
            .width(20)
          Text(this.message)
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })


        }
        .width('30%')
        //.border({ width: 2, color: 0x317af7, radius: 10, style: BorderStyle.Dotted })
        .margin({left:'35%',right:'35%',top:'2%'})
        Row(){
          Text('知乎').onClick(()=>{
            this.zhihu()
          })
            .width('100')
            .height('100')
            .fontSize(25)
            .margin({
              top:50,
              left:20,
            })
            .backgroundColor(Color.Black)
            .borderRadius(30)
            .padding(25)
            .fontColor(Color.White)
        }
        .width('100%')


        Row(){
          Image($r("app.media.faxian"))
            .width('10%')
            .margin({
              left:'10'
            })
            .onClick(()=>{
              this.faxian()
              this.col = '#00ff00'
            })
            .colorBlend(this.col)
          Image($r("app.media.shoucang"))
            .width('10%')
            .margin({
              left:'100'
            })
          Image($r("app.media.wode"))
            .width('10%')
            .margin({
              left:'100'
            })

        }
        .width('100%')
        .margin({
          top:'500',
          left:'30'
        })
      }
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Yellow)


  }
}