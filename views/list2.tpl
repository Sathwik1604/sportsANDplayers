<html>
<body>
<h2>Players</h2>
<hr/>
<table>
<tr>
    <th>NAME  </th>
    <th>AGE  </th>
    <th>SPORT  </th>
    <th>UPDATE  </th>
    <th>DELETE  </th>
  </tr>
% for pind in players:
  <tr>
    <td>{{pind["name"]}}</td>
    <td>{{pind["age"]}}</td>
    <td>{{pind["sport"]}}</td>
    <td><a href="/update2/{{str(pind['id'])}}">update</a></td>
    <td><a href="/delete2/{{str(pind['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<br>
<br>
<br>
<a href="/add2">Add new player</a>
<br>
<br>
<br>
<a href="/add1">Add new sport</a>
</body>
</html>