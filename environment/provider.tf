terraform {
  	required_providers {
        stackit = {
            source = "stackitcloud/stackit"
            version = ">=0.40.0"
        }
  	}
}

provider "stackit" {
   region = "eu01"
   enable_beta_resources = true
}
