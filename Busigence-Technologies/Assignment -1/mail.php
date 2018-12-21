<?php
if (mail("geekymano@gmail.com", "subject", "msgbody", "From: me@mydomain.com"))
    echo "mail sent";
  else
    echo "mail not sent";
 ?>