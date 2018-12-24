<template>
  <div class="limiter">
    <div class="container-login100">
      <div class="wrap-login100">
        <span class="login100-form-title">
						List of your own insurance policies
					</span>
        <table>
        <th>Type</th>
        <th> Start Date</th>
        <th> End Date</th>
        <th> Previously Insured </th>
        <th> Previously Damaged </th>
        <th> Cost of Product </th>
        <tbody>
        <tr v-for="elem in regPolicies" :key="elem.url" v-show="elem.RegPolicies_username == 'http://127.0.0.1:8000/api/regUsers/'+$session.get('username')+'/' " >
          <td> {{elem.RegPolicies_type}} </td>
          <td> {{elem.RegPolicies_startdate}} </td>
          <td> {{elem.RegPolicies_enddate}} </td>
          <td> {{elem.RegPolicies_previouslyInsured}} </td>
          <td> {{elem.RegPolicies_previouslyDamaged}} </td> 
          <td> {{elem.RegPolicies_costOfProduct}} </td>
         </tr>
         </tbody>
      </table>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  data () {
    return {

      regPolicies: []

    }
  },
  mounted: function() {

        
        axios.get('http://127.0.0.1:8000/api/regPolicies/').then(response => this.regPolicies = response.data).catch(error=> console.log(error))
    

    },
        }


</script>
<style>
  @import "./assets/main.css";
</style>








