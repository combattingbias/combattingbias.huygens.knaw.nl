---
hide:
  - navigation
  - toc
---

# Combatting Bias
<div class="cb-hero">
  <div>
    <p style="text-align: justify; margin-top: -7rem;">
    Combatting Bias is an initiative that has created a <strong>"bias-aware framework"</strong> to support researchers in identifying, describing, and reducing harmful biases in their data. 
    
    Rather than pursuing the impossible goal of complete bias elimination, this project provides <strong>guidelines for researchers to understand and transparently document biases</strong>. While predominantly focused on historical data, the framework provides a broad scope for any researcher or user to think about issues of bias in their work.</p>
  </div>
  <div>
    <img id="biasMapRotator" src="/static/img/bias-maps/1.png" style="width:190%; border-radius:8px;" alt="A map made of journal scraps, to represent bias as a concept">
    <p style="text-align:center; margin-top:.5rem;"><small style="color:#6b6b6b;">Bias Maps created by workshop participants</small></p>
    <script>
    (function () {
      const img = document.getElementById('biasMapRotator');
      if (!img) return;
      const images = Array.from({ length: 12 }, (_, i) => `/static/img/bias-maps/${i + 1}.png`);
      let idx = 0;
      setInterval(() => {
        idx = (idx + 1) % images.length;
        img.src = images[idx];
      }, 3000);
    })();
    </script>
  </div>
</div>
<!-- Cards Section -->
<div class="cb-grid">
  <div class="cb-card">
    <img src="/static/img/icons/toolkit.png" alt="Toolkit icon" class="cb-card-image">
    <h5>Combatting Bias Toolkit</h5>
    <p>The framework provides a broad scope for any researcher or user to think about issues of bias in their work.</p>
    <a href="bias/toolkit" class="md-button md-button--primary">Toolkit</a>
  </div>
  <div class="cb-card">
    <img src="/static/img/icons/vocabulary.png" alt="Vocabulary icon" class="cb-card-image">
    <h5>Vocabulary</h5>
    <p>Browse the bias vocabulary to establish a shared terminology across disciplines.</p>
    <a href="bias/types/about" class="md-button">Vocabulary</a>
  </div>
  <div class="cb-card">
    <img src="/static/img/icons/lifecycle.png" alt="Lifecycle icon" class="cb-card-image">
    <h5>Dataset Lifecycle</h5>
    <p>See where and how bias emerges at different stages of dataset creation and use.</p>
    <a href="lifecycle/about/" class="md-button">Lifecycle</a>
  </div>
</div>

<br>

<div class="cb-grid">
  <div class="cb-card">
    <h5>Ethical Commitments</h5>
    <p>Our mission to reduce harmful bias carries significant responsibility for research integrity and ethics.</p>
    <a href="bias/types/about" class="md-button">Ethical Commitments</a>
  </div>
  <div class="cb-card">
    <h5>Bias(ed) Maps</h5>
    <p>When many people come together to think about the question <i> what is bias?</i>: an activity in cutting and pasting.</p>
    <a href="bias/bias-maps" class="md-button">Bias(ed) Maps</a>
  </div>
  <div class="cb-card">
    <h5>Blog Posts</h5>
    <p>Newest: <i>When Archives Break Hearts</i> by Asawari Luthra</p>
    <a href="/news/when-archives-break-hearts" class="md-button md-button--primary">Read more!</a>
  </div>
</div>

<!-- Rest of your content -->
<hr>

<div class="flex-container" style="align-items: center; justify-content: space-between; margin-top: 10px;">
   <p class="text-block">Combatting Bias is funded by the <a href="https://nwo.nl" target="_top">Dutch Research Council (NWO)</a> via the  <a href="https://tdcc.nl" target="_blank">Thematic Digital Competence Centre Social Sciences & Humanities (TDCC-SSH)</a><br><br>
   Follow us on <a href="https://www.linkedin.com/company/combatting-bias/" target="_top">LinkedIn</a>!
   <!-- <a href="https://mastodon.social/@combattingbias" target="_top">Mastodon</a>, and <a href="https://bsky.app/profile/combattingbias.bsky.social" target="_top">Bluesky</a>!--><br><br>
Combatting Bias is hosted at the <a href="https://www.huygens.knaw.nl" target="_top">Huygens Institute</a>.
</p>
  <div class="logos-container" style="display: flex; flex-direction: column; gap: 4px;">
        <div class="image-block">
            <a href="https://tdcc.nl" target="_blank">
                <img src="./static/img/TDCC-SSH-Logo_RGB.png" alt="IISG logo"/>
            </a>
        </div>
        <div class="image-block">
            <a href="https://www.huygens.knaw.nl" target="_blank">
                <img src="/static/img/Huygens-Instituut-RGB.svg" alt="Huygens Institute logo" />
            </a>
        </div>
    </div>
</div>
