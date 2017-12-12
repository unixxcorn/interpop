# Internet Population
### Author : We have a plan. For : PSIT Project


### Detail
1. ข้อมูลที่เอามาใช้คืออะไร
  * ข้อมูลอัตราการใช้งานและจำนวนประชากรที่ใช้ คอมพิวเตอร์ โทรศัพท์มือถือ และ อินเทอร์เน็ต
2. เอามาจากไหนและมีจำนวนมากน้อยเพียงใด 
  * สำนักงานสถิติแห่งชาติ, http://service.nso.go.th/nso/web/survey/surtec5-1-3.html, พ.ศ. 2553 -.2559
3. จะวิเคราะห์อะไร
  * แนวโน้ม การใช้งาน การเติบโต และเวลาการใช้งาน คอมพิวเตอร์ โทรศัพท์มือถือ และการใช้อินเตอร์เน็ตของประชากรประเทศไทยตั้งแต่ปี พ.ศ.2553 - พ.ศ.2559
4. ผลและประโยชน์ที่คาดว่าจะได้โครงการนี้คืออะไร
  * นำข้อมูลไปช่วยวิเคราะห์วางแผนและพัฒนา ระบบสารสนเทศน์ ให้รองรับกับความต้องการของผู้ใช้
  * สามารถนำไปใช้วางแผนเพื่อพัฒนา เทคโนโลยี ให้ตรงกลุ่มเป้าหมายได้มากยิ่งขึ้น
5. โครงการนี้ความน่าสนใจตรงไหนบ้าง
  * เป็นข้อมูลที่มีความเกี่ยวข้องกับเทคโนโลยีสารสนเทศ
  * วิเคราะห์อัตราการใช้งานและจำนวนประชากรที่ใช้คอมพิวเตอร์ โทรศัพท์มือถือ และ อินเทอร์เน็ตได้
  * เป็นข้อมูลใกล้ตัว เหมาะกับการนำไปต่อยอดจากการเรียน
6. แตกต่างกับโครงการอื่นๆที่มีอยู่แล้วอะไรบ้าง 
  * มีข้อมูลย้อนหลังไปถึงปี พ.ศ. 2553 - 2559 ทำให้ข้อมูลมีความละเอียดและเข้าใจได้ง่ายยิ่งขึ้น     
7. URL รายละเอียดรายงานผลของโครงการจะเข้าไปดูได้ที่ไหน และ 
  * https://webserv.kmitl.ac.th/unixcorn/
8. URL github ของโครงการ ที่สามารถเข้าไปดู source code ได้
  * https://github.com/unixxcorn/we-have-a-plan

### Requirement
1. Python 3
2. Pygal
3. Pandas
4. Flask

### Install
1. Install Python3 using exe for windows or "apt-get install python3" for linux
2. Run "pip install pygal pandas flask" on your terminal or cmd
3. Open "run.bat" for windows or run "sh ./run.sh" on terminal for linux
4. Open your website
5. Ctrl+C to terminate

### GIT
#### Download https://git-scm.com/downloads
##### วิธีรีโหมด GIT // เปิดโฟล์เดอร์
* git init
* git remote add [ชื่อรีโหมด] https://github.com/unixxcorn/we-have-a-plan.git
##### วิธีดึงไฟล์  // เปิดดาวน์โหลด
* git pull -u [ชื่อรีโหมด] [branch]
##### วิธีดันไฟล์  // เปิดอัพโหลด
* git add [ชื่อไฟล์.นามสกุล]
* git commit -m "What do you want to say?"
* git push -u [ชื่อรีโหมด] [branch]
