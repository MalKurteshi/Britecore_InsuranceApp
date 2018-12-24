<template>
    <div class="limiter" >
        <div class="container-login100" >
            <div class="wrap-login100" style="width: 75%" >
                <form class="wrap-input100" v-on:submit.prevent="createANewRegPolicy" >

                    <span class="login100-form-title">
						Make your own insurance policy
					</span>

                    <div>
                        <div class="wrap-input100 validate-input"  data-validate = "Name is a required field">
                            Policy type:
                            <input class="input100" type="text" name="policyType" placeholder="" v-model="RegPolicies_type">
                            <span class="focus-input100"></span>
                        </div>

                        <div class="wrap-input100 validate-input" data-validate = "Required!!">
                            Choose start date for your insurance: 
                            <input class="input100" type="date" id="startDate" name="RiskStart" placeholder="" v-model="RegPolicies_startdate">
                            <span class="focus-input100"></span>
                        </div>

                        <div class="wrap-input100 validate-input" data-validate = "Required!!">
                            Choose end date for your insurance: 
                            <input class="input100" type="date" id="endDate" name="RiskEnd" placeholder="" v-model="RegPolicies_enddate">
                            <span class="focus-input100"></span>
                        </div>

                        <div class="wrap-input100 validate-input" data-validate = "Required!!">
                            Previously insured: <br>
                            <input  type="radio" id="PreviuslyInsuredYes" name="PreviuslyInsuredYes"  value="Yes" v-model="RegPolicies_previouslyInsured" />
                            <label for="PreviuslyInsuredYes">Yes  </label>
                            <input  type="radio" id="PreviuslyInsuredYes" name="PreviuslyInsuredYes"  value="No" v-model="RegPolicies_previouslyInsured" />
                            <label for="PreviuslyInsuredYes">No  </label>
                            <span class="focus-input100"></span>
                        </div>

                        <div class="wrap-input100 validate-input" data-validate = "Required!!">
                            Previously damaged: <br>
                            <input  type="radio" id="PreviuslyDamagedYes" name="PreviuslyDamagedYes"  value="Yes" v-model="RegPolicies_previouslyDamaged"/>
                            <label for="PreviuslyDamagedYes">Yes  </label>
                            <input  type="radio" id="PreviuslyDamagedYes" name="PreviuslyDamagedYes"  value="No" v-model="RegPolicies_previouslyDamaged"/>
                            <label for="PreviuslyDamagedYes">No  </label>
                            <span class="focus-input100"></span>
                        </div>

                        <div class="wrap-input100 validate-input" data-validate = "Required!!">
                            Birthday for human / Year or production for assets:
                            <input class="input100" type="date" id="Birthday" name="Birthday" placeholder="" v-model="RegPolicies_Bday_YearOfProduction">
                            <span class="focus-input100"></span>
                        </div>

                        <div class="wrap-input100 validate-input" data-validate = "Required!!">
                            Cost of the product:
                            <span >$</span>
                            <input class="input100" type="number" id="Cost" name="Cost"  step="any" placeholder="" style=" width: 50%" v-model="RegPolicies_costOfProduct" >
                            <span class="focus-input100"></span>
                        </div>

                        <div class="wrap-input100 validate-input" data-validate = "Desckription is required">
                            <label for="textarea">  Describe the product: </label>
                            <textarea class="input100" name="description" placeholder="" id="description" v-model="RegPolicies_description"> </textarea>
                            <span class="focus-input100"></span>
                        </div>

                    </div>

                    <div class="container-login100-form-btn">
                        <button class="login100-form-btn">
                            Submit the form
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {

  data () {
    return {
    RegPolicies_type: '',
    RegPolicies_startdate: '',
    RegPolicies_enddate: '',
    RegPolicies_previouslyInsured: '',
    RegPolicies_previouslyDamaged: '',
    RegPolicies_Bday_YearOfProduction: '',
    RegPolicies_costOfProduct: '',
    RegPolicies_description: '',
    RegPolicies_username: ''
    }
  },

  methods: {
      
    createANewRegPolicy() {
    axios.post('http://127.0.0.1:8000/api/regPolicies/', {
    RegPolicies_type: this.RegPolicies_type,
    RegPolicies_startdate: this.RegPolicies_startdate,
    RegPolicies_enddate: this.RegPolicies_enddate,
    RegPolicies_previouslyInsured: this.RegPolicies_previouslyInsured,
    RegPolicies_previouslyDamaged: this.RegPolicies_previouslyDamaged,
    RegPolicies_Bday_YearOfProduction: this.RegPolicies_Bday_YearOfProduction,
    RegPolicies_costOfProduct: this.RegPolicies_costOfProduct,
    RegPolicies_description: this.RegPolicies_description,
    RegPolicies_username: 'http://127.0.0.1:8000/api/regUsers/'+this.$session.get('username')+'/'
  })
  .then(function (response) {
    alert('The policy was created succesfully!!!!');
    console.log(response);
  })
  .catch(function (error) {
    alert('The policy was not created, please check your data and the input field and then try again!!!!');
    console.log(error);
  })
    this.RegPolicies_type = '' ;
    this.RegPolicies_startdate = '';
    this.RegPolicies_enddate = '';
    this.RegPolicies_previouslyInsured = '';
    this.RegPolicies_previouslyDamaged = '';
    this.RegPolicies_Bday_YearOfProduction = '';
    this.RegPolicies_costOfProduct = '';
    this.RegPolicies_description = '';
    this.RegPolicies_username = '' 
  
    }
  }
}
</script>

<style>
    @import "./assets/main.css";
</style>







