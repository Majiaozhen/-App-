import { router } from '@kit.ArkUI';

@Entry
@Component
struct Detail {
  @State message: string = '详情页';
  @State li: string[] = [];
  @State title: string[] = [];
  @State desc: string[] = [];
  aboutToAppear(){
    let data2 = router.getParams()
    let json_data = JSON.stringify(data2)
    let strData: string = json_data.substring(11);
    let list: string[] = strData.split(",");
    this.li = list
    for (let i = 0; i < list.length; i++){
      if (i%6 == 1) {
        this.title.push(list[i])
        this.desc.push(list[i+1])
      }
    }
    console.info("json_data:"+json_data)

  }


  build() {
    Column() {
      List(){
        ForEach(this.title, (item: string,index: number) => {
          ListItem(){
            Text(`${index+1} ${item}`+'\n    '+this.desc[index])
              .width('100%')
              .backgroundColor(Color.Black)
              .padding(10)
              .borderRadius(5)
              .fontColor(Color.White)
          }
          .padding(10)
          .backgroundColor(Color.Yellow)

        })
      }


    }
  }
}