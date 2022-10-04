def create_xml_body(ubi_num: int) -> str:
    return f"""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
      <ubiNum>{str(ubi_num)}</ubiNum>
    </NumberToWords>
  </soap12:Body>
</soap12:Envelope>"""
