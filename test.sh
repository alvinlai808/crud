echo -n "creating user alvin lai: "
curl -X POST http://127.0.0.1:5000/user\?fname\=alvin\&lname\=lai
echo ""
echo -n "creating user jennifer watanabe: "
curl -X POST http://127.0.0.1:5000/user\?fname\=jennifer\&lname\=watanabe
echo ""
echo -n "get alvin's last name: "
curl -X GET http://127.0.0.1:5000/user\?fname\=alvin
echo ""
echo -n "get jennifer's last name: "
curl -X GET http://127.0.0.1:5000/user\?fname\=jennifer
echo ""
echo -n "change alvin's last name to watanabe: "
curl -X PATCH http://127.0.0.1:5000/user\?fname\=alvin\&lname\=watanabe
echo ""
echo -n "change jennifer's last name to lai: "
curl -X PATCH http://127.0.0.1:5000/user\?fname\=jennifer\&lname\=lai
echo ""
echo -n "delete user alvin: "
curl -X DELETE http://127.0.0.1:5000/user\?fname\=alvin
echo ""
