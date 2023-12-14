<html>
<body>
<h2>Sports</h2>
<hr/>
<form action="/list1" method="get">
  <input name="query" placeholder="search"/>
  <button type="submit">Search</button>
</form>
<table>
<tr>
    <th>SPORT  </th>
    <th>CATEGORY  </th>
    <th>UPDATE  </th>
    <th>DELETE  </th>
  </tr>
% for sind in sports:
  <tr>
    <td>{{sind["name"]}}</td>
    <td>{{sind["category"]}}</td>
    <td><a href="/update1/{{str(sind['id'])}}">update</a></td>
    <td><a href="/delete1/{{str(sind['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<br>
<br>
<a href="/add1">Add new sport</a>
<br>
<br>
<br>
<a href="/add2">Add new Player</a>
</body>
</html>