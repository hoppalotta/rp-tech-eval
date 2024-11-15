resource "null_resource" "examples" {
  count = length(var.commands)
  provisioner "local-exec" {
    command = var.commands[count.index]
  }
}
