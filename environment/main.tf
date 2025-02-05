resource "stackit_server" "boot-from-volume" {
  project_id = "c1d81911-7b22-4171-b6df-21f71ec55dbd"
  name       = "terraform-server-test"
  boot_volume = {
    size        = 64
    source_type = "image"
    source_id   = "a2c127b2-b1b5-4aee-986f-41cd11b41279"
  }
  availability_zone = "eu01-1"
  machine_type      = "g1.1"
  keypair_name      = "sturm-cloud-key"
}
