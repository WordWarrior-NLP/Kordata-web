<script>
    export let event_list
    let portfolio_item = [...event_list]


</script>

<!-- Events Grid-->
<section class="page-section bg-light" id="portfolio">
    <div class="container">
        <div class="text-center">
            <h2 class="section-heading text-uppercase">TOP 10 사건</h2>
            <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
        </div>
        <div class="row">
            {#each portfolio_item as item, index}
                <div class="col-lg-4 col-sm-6 mb-4">
                    <div class="portfolio-item">
                        <a class="portfolio-link" data-bs-toggle="modal" href={`#portfolioModal${index+1}`}>
                            <div class="portfolio-hover">
                                <div class="portfolio-hover-content"><i class="fas fa-plus fa-3x"></i></div>
                            </div>
                            <img class="img-fluid" src={`src/assets/img/portfolio/${index+1}.jpg`} alt={item.name} />
                        </a>
                        <div class="portfolio-caption">
                            <div class="portfolio-caption-heading">{item.name}</div>
                            <div class="portfolio-caption-subheading text-muted">{item.datetime}</div>
                            <!--TODO : 사건 키워드 3개 또는 메인 기사 제목 삽입-->
                        </div>
                    </div>
                </div>
            {/each}
        </div>
    </div>
</section>