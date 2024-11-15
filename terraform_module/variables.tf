variable "commands" {
  type = list(string)
  default = [
    "echo 'Executed example1'",
    "echo 'Executed example2'",
    "echo 'Executed example3'"
  ]
}