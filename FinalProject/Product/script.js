document.addEventListener('DOMContentLoaded', () => {
    const synth = new Tone.PolySynth(Tone.Synth, {
        oscillator: { type: 'sine' },
        envelope: {
            attack: 0.5,
            decay: 0.5,
            sustain: 0.5,
            release: 0.5,
        }
    })

    // Create a filter and connect the synth to the filter, then to the destination.
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
    // Waveform selector interaction
    document.getElementById('waveformSelector').addEventListener('change', event => {
        synth.set({ oscillator: { type: event.target.value }});
    });

    // Envelope controls interaction
    const controls = ['attack', 'decay', 'sustain', 'release'];
    controls.forEach(param => {
        document.getElementById(param).addEventListener('input', event => {
            let value = parseFloat(event.target.value);
            synth.set({ envelope: { [param]: value } });
        });
    });


    // Filter cutoff frequency control
    const cutoff = document.getElementById('filterCutoff');
    const cutoffValueLabel = document.getElementById('cutoffValue');
    cutoff.addEventListener('input', function() {
        filter.frequency.value = this.value;
        cutoffValueLabel.textContent = `${this.value} Hz`; // Update the label dynamically
    });
});

