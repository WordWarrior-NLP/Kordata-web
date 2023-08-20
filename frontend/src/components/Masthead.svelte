<script>
    import { Link } from "svelte-routing"; 
    let subheading = "Welcome To Our Studio!"
    let greeting_txt = "It's Nice To Meet You"
    let main_btn_txt = "Tell Me More" 

</script>

<!-- Masthead-->
<header class="masthead">
    <div class="container">
        <div class="masthead-subheading">{subheading}</div>
        <div class="masthead-heading text-uppercase">{greeting_txt}</div>
        <Link class="btn btn-primary btn-xl text-uppercase" to="/events">{main_btn_txt}</Link>
    </div>
</header>