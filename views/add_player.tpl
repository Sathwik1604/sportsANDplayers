<html>
<body>
<h2>Add Player</h2>
<hr/>
<form action="/add2" method="post">
  <p>ADD New Player: <input name="name"/></p>
  <p>ADD Age: <input name="age"/></p>
  <p>ADD Sport: </p>
  <select name="sport">
  % for sport in sports:
    <option value="{{sport["id"]}}">{{sport["name"]}}</option>
  % end
  </select>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
</body>
</html>