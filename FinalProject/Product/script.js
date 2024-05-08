document.addEventListener('DOMContentLoaded', () => {
   
    const synth = new Tone.PolySynth(Tone.Synth, {

    })


    const filter = new Tone.Filter(2000, "lowpass").toDestination();
    synth.connect(filter);

    const keys = document.querySelectorAll('.key');
    keys.forEach(key => {
        key.addEventListener('mousedown', (event) => {
            const note = event.target.dataset.note;
            synth.triggerAttack(note);
        });
        key.addEventListener('mouseup', (event) => {
            const note = event.target.dataset.note;
            synth.triggerRelease(note);
        });
    });

    document.getElementById('waveformSelector').addEventListener('change', event => {
        synth.set({ oscillator: { type: event.target.value }});
    });


    const controls = ['attack', 'decay', 'sustain', 'release'];
    controls.forEach(param => {
        document.getElementById(param).addEventListener('input', event => {
            let value = parseFloat(event.target.value);
            synth.set({ envelope: { [param]: value } });
        });
    });


    
    const cutoff = document.getElementById('filterCutoff');
    const cutoffValueLabel = document.getElementById('cutoffValue');
    cutoff.addEventListener('input', function() {
        filter.frequency.value = this.value;
        cutoffValueLabel.textContent = `${this.value} Hz`; 
    });
});

