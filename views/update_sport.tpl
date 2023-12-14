<html>
<body>
<h2>Update sport</h2>
<hr/>
<form action="/update1" method="post">
  <input type="hidden" name="id" value="{{id}}"/>
  <p>Name: <input name="name" value="{{name}}"/></p>
  <p>category: <input name="category" value="{{category}}"/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
</body>
</html>