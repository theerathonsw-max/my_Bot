# 🔑 ENVIRONMENT VARIABLES GUIDE

> คำแนะนำวิธีการใส่คีย์ (Environment Variables) สำหรับบอท Discord

---

## 📋 ตัวแปรที่ต้อง (Required)

### 1. TOKEN 🤖

**คืออะไร:** Discord Bot Token  
**ที่ไป:** ที่นี่ไปใส่ token ของบอท Discord

#### วิธีสร้าง Token:

```
1. ไปที่ https://discord.com/developers/applications
2. เลือก Application ของคุณ
3. ไปที่ Tab "Bot" ด้านซ้าย
4. ดู "TOKEN" section
5. คลิก "Copy" เพื่อคัดลอก
```

#### ตัวอย่าง Token:
```
TOKEN=MTk4NjIyNDgzNTgxOTI4MzI0.Clwa7A.l7r3XoLnN78OPVPh6K1ByGrqaco
```

**⚠️ สำคัญ:** อย่าบอก token ให้ใคร! มันเหมือนรหัสผ่าน!

---

## ⚙️ ตัวแปรเพิ่มเติม (Optional)

### 2. PREFIX ⌨️

**คืออะไร:** สัญลักษณ์เริ่มต้นของคำสั่ง  
**ค่าเริ่มต้น:** `/`

#### ตัวอย่าง:

```bash
PREFIX=/
# คำสั่ง: /help, /admin, /fun

PREFIX=!
# คำสั่ง: !help, !admin, !fun

PREFIX=$
# คำสั่ง: $help, $admin, $fun
```

### 3. OWNER_ID 👤

**คืออะไร:** Discord ID ของเจ้าของบอท  
**ทำไมต้อง:** บางคำสั่งใช้แค่ owner ได้

#### วิธีหา ID:

```
1. เปิด Discord
2. Settings → Advanced
3. เปิด "Developer Mode"
4. ขวาคลิกชื่อของคุณ
5. "Copy User ID"
```

#### ตัวอย่าง:
```bash
OWNER_ID=123456789
```

### 4. DEBUG 🐛

**คืออะไร:** โหมด Debug  
**ค่า:** `true` หรือ `false`

#### ตัวอย่าง:

```bash
DEBUG=true
# แสดงข้อมูลเยอะ สำหรับพัฒนา

DEBUG=false
# ปกติ (ใช้กับ Production)
```

---

## 🚀 วิธีการใส่ Environment Variables

### วิธีที่ 1: Render Dashboard (แนะนำ)

#### ขั้นตอน:

```
1. ไปที่ https://render.com
2. Dashboard → Your Service
3. ไปที่ Tab "Environment"
4. คลิก "Add Environment Variable"
```

#### ใส่ข้อมูล:

```
Variable Name: TOKEN
Value: (paste bot token ที่นี่)
→ Save

Variable Name: PREFIX
Value: /
→ Save

Variable Name: OWNER_ID
Value: (your discord id)
→ Save

Variable Name: DEBUG
Value: false
→ Save
```

#### ผลลัพธ์:
```
✅ TOKEN = MTk4NjIyNDgz...
✅ PREFIX = /
✅ OWNER_ID = 123456789
✅ DEBUG = false
```

---

### วิธีที่ 2: .env File (สำหรับทำงานในเครื่อง)

#### สร้างไฟล์:

```bash
# สร้างไฟล์: .env
# ในโฟลเดอรเดียวกับ main.py
```

#### ใส่ข้อมูล:

```env
# .env file
TOKEN=MTk4NjIyNDgzNTgxOTI4MzI0.Clwa7A.l7r3XoLnN78OPVPh6K1ByGrqaco
PREFIX=/
OWNER_ID=123456789
DEBUG=false
```

#### สำคัญ!

```bash
# ใส่ใน .gitignore
echo ".env" >> .gitignore

# ไม่ให้ .env ขึ้น GitHub!
```

---

### วิธีที่ 3: config.json (ทางเลือก)

#### สร้างไฟล์:

```json
{
  "TOKEN": "MTk4NjIyNDgzNTgxOTI4MzI0.Clwa7A...",
  "PREFIX": "/",
  "OWNER_ID": 123456789,
  "DEBUG": false
}
```

#### สำคัญ!

```bash
# ใส่ใน .gitignore
echo "config.json" >> .gitignore
```

---

## 🔍 วิธีตรวจสอบ

### ใน Render:

```
1. Dashboard → Environment
2. ดู variables ที่คุณใส่
3. โปรดอย่าบอก TOKEN ให้คนอื่น
```

### ในเครื่อง:

```bash
# ตรวจสอบ .env
cat .env

# ผลลัพธ์ต้องเห็น:
# TOKEN=...
# PREFIX=/
# OWNER_ID=123456789
# DEBUG=false
```

---

## ⚠️ Security Tips

### 1. ไม่ให้ Token ลงเน็ต

```bash
❌ ผิด:
TOKEN=abc123 git push

✅ ถูก:
# ใส่ใน .env หรือ Environment Variables เท่านั้น
```

### 2. ไม่ให้ Push config.json

```bash
# .gitignore
.env
config.json
*.log
```

### 3. Rotate Token ถ้าลงเน็ต

```
1. Discord Developer Portal
2. Bot → Regenerate TOKEN
3. ใส่ TOKEN ใหม่
```

### 4. ใช้ Environment Variables ใน Production

```bash
# ❌ ผิด (ไม่ใช้ config file)
TOKEN=abc123 python main.py

# ✅ ถูก (ใช้ env vars)
# ใส่ใน Render Environment atau .env
```

---

## 🎯 Quick Reference

| Variable | Type | ตัวอย่าง | Required |
|----------|------|---------|----------|
| TOKEN | string | `MTk4NjI...` | ✅ Yes |
| PREFIX | string | `/` | ❌ No |
| OWNER_ID | number | `123456789` | ❌ No |
| DEBUG | boolean | `false` | ❌ No |

---

## 🚀 Deploy Steps

### Step 1: สร้าง .env
```bash
echo "TOKEN=your_token" > .env
echo "PREFIX=/" >> .env
echo "OWNER_ID=your_id" >> .env
```

### Step 2: Render Environment

```
1. Dashboard → Environment
2. Add TOKEN, PREFIX, OWNER_ID
3. Save
```

### Step 3: Deploy

```
1. Render Dashboard
2. Click "Deploy"
3. Done! ✅
```

---

## ❓ FAQ

**Q: ที่ไหนดึง TOKEN?**  
A: https://discord.com/developers/applications → Bot → TOKEN

**Q: ของหมด TOKEN ได้ไหม?**  
A: ได้ คลิก "Regenerate" ใน Developer Portal

**Q: TOKEN ต้องหมุนเวียนไหม?**  
A: ไม่ต้อง แต่ถ้า leak ให้ regenerate ทันที

**Q: .env ต้องขึ้น GitHub ไหม?**  
A: ไม่! ใส่ใน .gitignore

**Q: สามารถใส่ที่ config.json ได้ไหม?**  
A: ได้ แต่ Render environment ดีกว่า

---

## 📞 Support

ถ้ามีปัญหา:
1. ตรวจสอบ TOKEN ถูกต้องหรือไม่
2. ตรวจสอบ .gitignore มี .env ไหม
3. ตรวจสอบ Render Environment Variables

---

**✅ ตั้งค่า Environment Variables สำเร็จ!**

*Made with ❤️ | Secure Your Bot!*
