<script>
    let portfolio_heading = ["Thread", "Explore", "Finish", "Lines","Southwest", "Window"]
    let portfolio_text = ["Illustration", "Graphic Design","Identity", "Branding","Website Design","Photography"]

</script>

<!-- Portfolio Grid-->
<section class="page-section bg-light" id="portfolio">
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">Portfolio</h2>
            <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
        </div>
        <div class="row">
            {#each portfolio_heading as heading, index}
                <div class="col-lg-4 col-sm-6 mb-4">
                    <!-- Portfolio item-->
                    <div class="portfolio-item">
                        <a class="portfolio-link" data-bs-toggle="modal" href={`#portfolioModal${index+1}`}>
                            <div class="portfolio-hover">
                                <div class="portfolio-hover-content"><i class="fas fa-plus fa-3x"></i></div>
                            </div>
                            <img class="img-fluid" src={`src/assets/img/portfolio/${index+1}.jpg`} alt="..." />
                        </a>
                        <div class="portfolio-caption">
                            <div class="portfolio-caption-heading">{heading}</div>
                            <div class="portfolio-caption-subheading text-muted">{portfolio_text[index]}</div>
                        </div>
                    </div>
                </div>
            {/each}
        </div>
    </div>
</section>