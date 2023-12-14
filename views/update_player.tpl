<html>
<body>
<h2>Update player</h2>
<hr/>
<form action="/update2" method="post">
  <input type="hidden" name="id" value="{{id}}"/>
  <p>Name: <input name="name" value="{{name}}"/></p>
  <p>Age: <input name="age" value="{{age}}"/></p>
  <p>Sport: 
  <select name="sport">
  % for sport in sports:
    <option value="{{sport["id"]}}">{{sport["name"]}}</option>
  % end
  </select>
  </p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
</body>
</html>