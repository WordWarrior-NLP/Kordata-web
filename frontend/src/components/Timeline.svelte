<script>
    
    let timeline_heading = ["March 2011", "December 2015", "July 2020"]
    let timeline_subheading = ["An Agency is Born","Transition to Full Service","Phase Two Expansion"]
    let timeline_body = [
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit.", 
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit.", 
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit."
    ]

</script>
<!-- About-->
 <section class="page-section" id="about">
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">About</h2>
            <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
        </div>
        <ul class="timeline">
            {#each timeline_heading as heading, index}
                <li class:timeline-inverted={index%2 === 1}>  <!--중괄호 안의 조건식이 참일 때에만 class 부여-->
                    <div class="timeline-image"><img class="rounded-circle img-fluid" src={`src/assets/img/about/${index+1}.jpg`} alt="..." /></div>
                    <div class="timeline-panel">
                        <div class="timeline-heading">
                            <h4>{heading}</h4>
                            <h4 class="subheading">{timeline_subheading[index]}</h4>
                        </div>
                        <div class="timeline-body"><p class="text-muted">{timeline_body[index]}</p></div>
                    </div>
                </li>
            {/each}
            <li class="timeline-inverted">
                <div class="timeline-image">
                    <h4>
                        Be Part
                        <br />
                        Of Our
                        <br />
                        Story!
                    </h4>
                </div>
            </li>
        </ul>
    </div>
</section>