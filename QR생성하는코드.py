{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c91896c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import qrcode\n",
    "\n",
    "# QR 코드로 만들 URL\n",
    "url = \"https://github.com/DVSY7/Open-API\"\n",
    "\n",
    "# QR 코드 생성\n",
    "qr = qrcode.QRCode(\n",
    "    version=1,  # QR 코드 크기 (1~40)\n",
    "    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 정정 수준\n",
    "    box_size=10,  # 박스 크기\n",
    "    border=4,  # 테두리 두께\n",
    ")\n",
    "\n",
    "qr.add_data(url)\n",
    "qr.make(fit=True)\n",
    "\n",
    "# 이미지로 변환\n",
    "img = qr.make_image(fill_color=\"black\", back_color=\"white\")\n",
    "\n",
    "# 저장\n",
    "img.save(\"streamlit_qr.png\")\n",
    "\n",
    "# 보기 (옵션)\n",
    "img.show()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
