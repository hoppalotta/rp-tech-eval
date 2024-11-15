resource "null_resource" "example1" {
  provisioner "local-exec" {
    command = "echo 'Executed example1'"
  }
}

resource "null_resource" "example2" {
  provisioner "local-exec" {
    command = "echo 'Executed example2'"
  }
}

resource "null_resource" "example3" {
  provisioner "local-exec" {
    command = "echo 'Executed example3'"
  }
}
