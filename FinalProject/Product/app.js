document.addEventListener('DOMContentLoaded', () => {
    const synth = new Tone.Synth({
        oscillator: { type: 'sine' },
        envelope: {
            attack: 0.5,
            decay: 0.2,
            sustain: 0.5,
            release: 1
        }
    }).toDestination();

    window.noteOn = function(event) {
        const note = event.target.dataset.note;
        synth.triggerAttack(note);
    };

    window.noteOff = function(event) {
        synth.triggerRelease();
    };

    document.getElementById('waveformSelector').addEventListener('change', event => {
        synth.oscillator.type = event.target.value;
    });

    const controls = ['attack', 'decay', 'sustain', 'release'];
    controls.forEach(param => {
        document.getElementById(param).addEventListener('input', event => {
            synth.envelope[param] = parseFloat(event.target.value);
        });
    });
});
