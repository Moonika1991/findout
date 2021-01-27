from findout.Connectors import Connectors

search = 'or(search(a,"example"),search(b,"another example"))  search(c,"code") '

sc = Connectors()

print(sc.validate(sc.parse(search)))
